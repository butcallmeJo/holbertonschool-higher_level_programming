//
//  ViewController.swift
//  TapperProject
//
//  Copyright © 2016 Holberton School. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    // Mark: Properties
    @IBOutlet weak var image_tapper: UIImageView!
    @IBOutlet weak var button_play: UIButton!
    @IBOutlet weak var textfield_number: UITextField!
    @IBOutlet weak var button_coin: UIButton!
    @IBOutlet weak var label_taps: UILabel!
    
    var taps_done: Int = 0
    var taps_requested: Int = 10
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        resetGame()
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    // Mark: Actions
    @IBAction func clickPlayButton(sender: AnyObject) {
        let str = textfield_number.text
        
        let num = Int(str!)
        
        if num < 1 {
            return
        }
        taps_requested = num!
        print("let's do " + String(num!) + " taps")
        initGame()

    }

    @IBAction func clickCoinButton(sender: AnyObject) {
        taps_done += 1
        label_taps.text = String(taps_done) + " Taps"
        print("" + String(taps_done) + " Tap!")
        
        if taps_done >= taps_requested {
            resetGame()
        }
    }
    
    func initGame() {
        image_tapper.hidden = true
        button_play.hidden = true
        label_taps.hidden = false
        button_coin.hidden = false
        textfield_number.hidden = false
        taps_done = 0
        label_taps.text = "0 Taps"
    }
    
    func resetGame() {
        image_tapper.hidden = false
        button_play.hidden = false
        label_taps.hidden = true
        button_coin.hidden = true
        textfield_number.hidden = true
        taps_requested = 0
    }
    
}

