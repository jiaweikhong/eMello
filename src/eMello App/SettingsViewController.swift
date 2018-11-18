//
//  SettingsViewController.swift
//  eMello
//
//  Created by eMelloTeam on 2018/6/5.
//  Copyright © 2018 testing. All rights reserved.
//

import UIKit

/* This ViewController deals with the Settings Page
 Currently, the Settings page toggles the autoplay of BGM and allows the user to view credits.
 */

class SettingsViewController: UIViewController {
    
    //MARK: Properties
    var bookArray = [Book]()
    var TutorialCounter = 0
    
    //MARK: Music Properties
    @IBOutlet weak var BGMSwitch: UISwitch!
    var BGM:Bool?
    var settingsBGM:Bool?
    
    //MARK: BGM Function
    @IBAction func toPlayBGM(_ sender: Any) {
        
        if BGMSwitch.isOn{
            settingsBGM = true
            print("Autopay BGM Switch is ON")
            //play BGM
        }
            
        else{
            settingsBGM = false
            print("Default BGM Switch is off")
            //don't play BGM
        }
    }
    
    //MARK: Navigations
    @IBAction func goToHomeCancel(_ sender: Any) {
        
        let homePage = self.storyboard?.instantiateViewController(withIdentifier: "HomePage") as! HomeViewController
        
        //Update bookArray in Librarypage
        homePage.bookArray = bookArray
        print("Home page is updated from Settings")
        print("Bookarray in Home: \(homePage.bookArray)")
        
        //BGM Settings
        homePage.BGM = BGM
        print(BGM!)
        print("No changes made")
        
        //Tutorial Settings
        homePage.TutorialCounter = TutorialCounter
        print("Tutorial counter: \(TutorialCounter)")
        
        print("Going to Home page")
        self.present(homePage, animated: true, completion: nil)
    }
    
    @IBAction func goToHomeWithComfirm(_ sender: Any) {
        
        let homePage = self.storyboard?.instantiateViewController(withIdentifier: "HomePage") as! HomeViewController
        
        //Update bookArray in Librarypage
        homePage.bookArray = bookArray
        print("Home page is updated from Settings")
        print("Bookarray in Home: \(homePage.bookArray)")
        
        //BGM Settings
        homePage.BGM = settingsBGM
        print("New settings have been saved")
        
        //Tutorial Settings
        homePage.TutorialCounter = TutorialCounter
        print("Tutorial counter: \(TutorialCounter)")
        
        print("Going to Home page")
        self.present(homePage, animated: true, completion: nil)
    }
    
    //MARK: About Us
    @IBOutlet weak var AboutUsView: UIView!
    @IBOutlet weak var DesignStatement: UILabel!
    @IBOutlet weak var Credits: UILabel!
    @IBAction func goToAboutUs(_ sender: UIButton) {
        //Just open up a pop up
        AboutUsView.isHidden = false
        //Include credits
    }
    
    @IBAction func dismissAboutUs(_ sender: UITapGestureRecognizer) {
        AboutUsView.isHidden = true
    }
    
    //MARK: Initialization
    override func viewDidLoad() {
        super.viewDidLoad()
        print("Settings page loaded")
        print("Setting BGM Switch")
        BGMSwitch.setOn(BGM!, animated: false)
        settingsBGM = BGM!
        print("Status of Default BGM Switch \(BGMSwitch.isOn)")
        
        AboutUsView.isHidden = true
        
        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    
}
