//
//  TechCompaniesListViewController.swift
//  TechCompanies
//
//  Created by Josquin Gaillard on 6/8/16.
//  Copyright © 2016 Josquin Gaillard. All rights reserved.
//

import UIKit

class TechCompaniesListViewController: UITableViewController {
    
    var schoolList: [Entity]!
    var techCompanyList: [Entity]!
    let techDetailSegue = "techDetailSg"

    override func viewDidLoad() {
        super.viewDidLoad()
        self.title = "Silicon Valley Entities"
        techCompanyList = EntitiesHelper.getTechCompanies()
        schoolList = EntitiesHelper.getSchools()

        // Uncomment the following line to preserve selection between presentations
        // self.clearsSelectionOnViewWillAppear = false

        // Uncomment the following line to display an Edit button in the navigation bar for this view controller.
        // self.navigationItem.rightBarButtonItem = self.editButtonItem()
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    // MARK: - Table view data source

    override func numberOfSectionsInTableView(tableView: UITableView) -> Int {
        // #warning Incomplete implementation, return the number of sections
        return 2
    }

    override func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        // #warning Incomplete implementation, return the number of rows
        if section == 0 {
            // return # of companies as # of rows
            return techCompanyList.count
        }
        else {
            // return # of schools as # of rows
            return schoolList.count
        }
    }

    override func tableView(tableView: UITableView, titleForHeaderInSection section: Int) -> String? {
        // return title for section
        if section == 0 {
            return "Tech Companies"
        }
            
        else {
            return "Schools"
        }
    }
    
    override func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCellWithIdentifier("techCell", forIndexPath: indexPath)

        // Configure the cell...

        if indexPath.section == 0 {
            cell.textLabel?.text = techCompanyList[indexPath.row].name
            cell.detailTextLabel?.text = "I love working"
        }
            
        else if indexPath.section == 1 {
            cell.textLabel?.text = schoolList[indexPath.row].name
            cell.detailTextLabel?.text = "I love studying"
        }
        
        return cell
    }


    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
        print ("TESSSTTT")
        if segue.identifier == "techDetailSegue" {
            print ("segue works test")
            let indexPath = self.tableView.indexPathForCell(sender as! UITableViewCell)
            
            if let destinationViewController = segue.destinationViewController as? TechCompanyDetailViewController { // set destination vc to detail view controller
                print ("destinationViewController thingy test")
                // if cast was successful,
                // pass appropriate entity to represent to new view controller, according to section and row.
                if indexPath!.section == 0 {
                    destinationViewController.entity = techCompanyList[indexPath!.row]
                    print (techCompanyList[indexPath!.row])
                    print ("test")
                }
                else if indexPath!.section == 1 {
                    destinationViewController.entity = schoolList[indexPath!.row]
                }
            }
        }
    }


}
