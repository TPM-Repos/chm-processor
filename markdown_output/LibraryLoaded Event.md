Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
LibraryLoaded Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Extensibility Namespace](topic1995.md) > [ILibraryManager Interface](topic2079.md) : LibraryLoaded Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Occurs when a library has been loaded into the application. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event LibraryLoaded As [LibraryEventHandler](topic2155.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ILibraryManager](topic2079.md)
    Dim handler As [LibraryEventHandler](topic2155.md)
     
    AddHandler instance.LibraryLoaded, handler  
  
C#|   
---|---  
      
    
    event [LibraryEventHandler](topic2155.md) LibraryLoaded  
  
# Event Data

The event handler receives an argument of type [LibraryEventArgs](topic2124.md) containing data related to this event. The following **LibraryEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[LibraryInfo](topic2131.md)| Gets information about the library that was loaded.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ILibraryManager Interface](topic2079.md)   
[ILibraryManager Members](topic2080.md)


