//
//  BookModel.swift
//  eMello
//
//  Created by eMelloTeam on 2018/6/28.
//  Copyright © 2018 testing. All rights reserved.
//

import Foundation

/* This class is an array of books that will be stored in the Library/Bookshelf.
 */

class BookModel {

    func getBooks() -> [Book] {
        var array = [Book]()
        let bellabook = Book()
        bellabook.imageName = "BellaTheDragonRA"
        array.append(bellabook)
        return array    // Returns an array hardcoded to have just the bellabook
    }

    //Try to load all sample books
    func loadSampleBooks() -> [Book]{
        var sampleArray = [Book]()
        
        //Initializing properties for "FindingAFriend".
        let mermaid = Book()
        mermaid.imageName = "Mermaid"
        mermaid.pageType = "html"
        mermaid.page = "FindingAFriend/"
        mermaid.totalpages = 14
        mermaid.songType = "mp3"
        mermaid.songs = ["","BGM/Strings of Time", "BGM/Tiny Kingdom", "BGM/Forest Ventures", "BGM/All Shall End", "BGM/I Walk Alone", "BGM/Fireplace Thinking", "BGM/The Power Of", "BGM/Healing", "BGM/Father forgive them", "BGM/Tears of Joy", "BGM/Times", "BGM/A New Way", "BGM/A Fresh Thought", "BGM/Our Memories"]
        
        //Initializing properties for "BellaTheDragon".
        let bellabook = Book()
        bellabook.name = "Bella The Dragon"
        bellabook.imageName = "BellaTheDragonRA"
        bellabook.pageType = "html"
        bellabook.page = "BellaDragon/OEBPS/"
        bellabook.totalpages = 23
        bellabook.songType = "mp3"
        bellabook.songs = ["","","BGM/The Town of Our Youth", "BGM/A New Way", "BGM/Life at the Inn", "BGM/Blue Skies", "BGM/Dreams of a Child", "BGM/Forest Ventures", "BGM/Tiny Kingdom", "BGM/Land of Fantasy", "BGM/Mystery Forest", "BGM/Broken Village", "BGM/Sad Winds Chap 1", "BGM/Sad Winds Chap 2", "BGM/Forgotten", "BGM/The Quiet Morning", "BGM/City of Ruins", "BGM/Goodbye, My Friend", "BGM/Fireplace Thinking", "BGM/I Still Feel Your Heart", "BGM/Healing", "BGM/Skies", "BGM/Tears of Joy", "BGM/Happy Dreams"]
        
        //Properties of the upload book button.
        let addbook = Book()
        //addbook.name = ""
        addbook.imageName = "Book plus"
        //addbook.pageType = "xhtml"
        //addbook.page = ""
        //addbook.totalpages = 22
        //addbook.songs = ["BGM/JewelBeat - Happy Moments","BGM/JewelBeat - Jazz Lounge","BGM/JewelBeat - Happy Moments","BGM/JewelBeat - Jazz Lounge","BGM/JewelBeat - Happy Moments","BGM/JewelBeat - Jazz Lounge","BGM/JewelBeat - Happy Moments","BGM/JewelBeat - Jazz Lounge","BGM/JewelBeat - Happy Moments","BGM/JewelBeat - Jazz Lounge"]
        
        sampleArray += [mermaid,bellabook, addbook]
        return sampleArray
    }
}
