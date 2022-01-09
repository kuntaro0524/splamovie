import cv2,sys

class AnaMP4:
    def __init__(self, filename):
        # Input movie file
        self.infile = filename
        # "Gachi" template image
        self.title_template = "../Templates/gachi.png"
        # Death template image
        self.death_template = "../Templates/death.png"
        # Kill template image
        self.kill_template = "../Templates/template_killed.png"

        self.isInit = False

        # Time series
        self.time_series = []

    def templateMatch(self, target_cvimage, template_cvimage):
        # print("{} and {} are compared".format(target_cvimage, template_cvimage))
        result = cv2.matchTemplate(target_cvimage, template_cvimage, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        return (max_val)

    def init(self):
        # ビデオキャプチャ
        self.video = cv2.VideoCapture(self.infile)
        # フレーム数
        self.frame_count = int(self.video.get(7)) 
        # フレームレート
        self.frame_rate = int(self.video.get(5))

        self.isInit=True
        print("initialization finished.")

    def findDeathScene(self):
        if self.isInit == False: self.init()

        # グレースケールでテンプレート画像を読み込む
        temp = cv2.imread(self.death_template, 0)

        # death time
        deadTime = 0
        dead = [] 
        
        # an interval time to extract images
        inttime = 5
        # number of images to be analyzed
        n_ana = int(self.frame_count / self.frame_rate / inttime)
        print("{} images are analyzed".format(n_ana))

        for i in range(0, n_ana):
            # このフレームが開始後何秒に相当するか
            t_from_start = inttime * i
            # print("{}フレームだよ".format(self.frame_rate * t_from_start))
            self.video.set(1 , self.frame_rate * t_from_start)
            _, frame = self.video.read()
            framegray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 

            cv2.imwrite("frame_%02d.png"%i, framegray)

            # テンプレートが取得した画像に存在するかどうかを確認
            checkVal = self.templateMatch(framegray,temp); 
            # print(i, checkVal)

            # テンプレート画像が見つかった場合にはフレーム番号などを取得する
            if checkVal > 0.8:
                target_time = t_from_start
                print ("{} sec is matched.".format(target_time))
                dead.append(target_time)
        return dead


    def findDeathKillScenes(self):
        if self.isInit == False: self.init()

        # グレースケールでテンプレート画像を読み込む
        death_template = cv2.imread(self.death_template, 0)
        kill_template = cv2.imread(self.kill_template,0)

        # death time
        deadTime = 0
        deads = [] 
        kills = []

        # an interval time to extract images
        inttime = 5
        # number of images to be analyzed
        n_ana = int(self.frame_count / self.frame_rate / inttime)
        print("{} images are analyzed".format(n_ana))

        for i in range(0, n_ana):
            # このフレームが開始後何秒に相当するか
            t_from_start = inttime * i
            # print("{}フレームだよ".format(self.frame_rate * t_from_start))
            self.video.set(1 , self.frame_rate * t_from_start)
            _, frame = self.video.read()
            # framegray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
            framegray = cv2.cvtColor(frame, 0) 
            # テンプレートが取得した画像に存在するかどうかを確認
            check_death = self.templateMatch(framegray,death_template)
            # テンプレートが取得した画像に存在するかどうかを確認
            check_kill = self.templateMatch(framegray,kill_template)

            print(check_death, check_kill)

            # テンプレート画像が見つかった場合にはフレーム番号などを取得する
            if check_death > 0.8:
                deads.append(t_from_start)
            # テンプレート画像が見つかった場合にはフレーム番号などを取得する
            if check_kill > 0.8:
                kills.append(t_from_start)

        return deads, kills

    def findAll(self):
        if self.isInit == False: self.init()

        # グレースケールでテンプレート画像を読み込む
        death_tmp = cv2.imread(self.death_template)
        kill_tmp = cv2.imread(self.kill_template)
        title_tmp = cv2.imread(self.title_template)

        death_temp = cv2.cvtColor(death_tmp, cv2.COLOR_BGR2GRAY) 
        kill_temp = cv2.cvtColor(kill_tmp, cv2.COLOR_BGR2GRAY) 
        title_temp = cv2.cvtColor(title_tmp, cv2.COLOR_BGR2GRAY) 

        # death time
        deadTime = 0
        deads = [] 
        kills = []
        titles = []

        # an interval time to extract images
        inttime = 5
        # number of images to be analyzed
        n_ana = int(self.frame_count / self.frame_rate / inttime)
        print("{} images are analyzed".format(n_ana))

        for i in range(0, n_ana):
            # このフレームが開始後何秒に相当するか
            t_from_start = inttime * i
            # print("{}フレームだよ".format(self.frame_rate * t_from_start))
            self.video.set(1 , self.frame_rate * t_from_start)
            _, frame = self.video.read()
            framegray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
            cv2.imwrite("frame_%04d.png"%i, framegray)

            # テンプレートが取得した画像に存在するかどうかを確認
            check_death = self.templateMatch(framegray,death_temp)
            # テンプレートが取得した画像に存在するかどうかを確認
            check_kill = self.templateMatch(framegray,kill_temp)
            # タイトルが表示されているかどうか
            check_title = self.templateMatch(framegray,title_temp)

            print(check_death, check_kill, check_title)

            # テンプレート画像が見つかった場合にはフレーム番号などを取得する
            if check_death > 0.8:
                deads.append(t_from_start)
            # テンプレート画像が見つかった場合にはフレーム番号などを取得する
            if check_kill > 0.8:
                kills.append(t_from_start)
            # テンプレート画像が見つかった場合にはフレーム番号などを取得する
            if check_title > 0.8:
                titles.append(t_from_start)

        return deads, kills, titles

if __name__ == '__main__':
    am = AnaMP4(sys.argv[1])
    print(am.findAll())