// Script that describes a Person based on input given by a main func

// super class for Person. init name and age
class Person {
  var first_name: String
  var last_name: String
  var age: Int

  init(first_name: String, last_name: String, age: Int) {
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
  }

  // func that returns the full name of Person
  func fullName() -> String {
    return "\(self.first_name) \(self.last_name)"
  }
}

// protocol that classifies a Person as a student or mentor
protocol Classify {
  func isStudent() -> Bool
}

// enum to define the type of subject done by a mentor
enum Subject {
  case Math
  case English
  case French
  case History
}

// sub-class of Person to describe mentors
class Mentor: Person, Classify {
  let subject: Subject
  // overloading constructor
  init(first_name: String, last_name: String, age: Int, subject: Subject = Subject.Math) {
    self.subject = subject
    super.init(first_name: first_name, last_name: last_name, age: age)
  }

  // func that returns the subject as a String
  func stringSubject() -> String {
    switch subject {
      case .Math: return "Math"
      case .English: return "English"
      case .French: return "French"
      case .History: return "History"
    }
  }
  // func that returns false because Person is not student
  func isStudent() -> Bool {
    return false
  }
}

// sub-class of Person to describe students
class Student: Person, Classify {
  // func that returns true because Person is student
  func isStudent() -> Bool {
    return true
  }
}

// class school where Person (student or mentor) can be added to
class School {
  var name: String
  var list_persons: [Person]
  // constructor
  init(name: String) {
    self.name = name
    self.list_persons = []
  }

  // function to add p to the attribute list_persons
  func addStudent(p: Person) -> Bool {
    // if p is student, add to list_persons and return true
    if p is Student {
      list_persons.append(p)
      return true
    } else {
      return false
    }
  }
  // function to add p to the attribute list_persons
  func addMentor(p: Person) -> Bool {
    // if p is mentor, add to list_persons and return true
    if p is Mentor {
      list_persons.append(p)
      return true
    } else {
      return false
    }
  }

  // function to return the list of Students from oldest to youngest
  func listStudents() -> [Person] {
    list_persons.filter($0 is Student) {
      return $0.age < $1.age
    }
  }
  // function to return the list of Mentors from oldest to youngest
  func listMentors() -> [Person] {
    list_persons.filter($0 is Mentor) {
      return $0.age < $1.age
    }
  }
  // function to return the list of Mentors of subject from oldest to youngest
  func listMentorsBySubject(x) -> [Person] {
    list_persons.filter($0 is Mentor && $0.subject is x) {
      return $0.age < $1.age
    }
  }
}
