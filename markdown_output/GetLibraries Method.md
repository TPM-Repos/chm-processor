Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetLibraries Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Extensibility Namespace](topic1995.md) > [ILibraryManager Interface](topic2079.md) : GetLibraries Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets an array of the libraries that are loaded into the application. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetLibraries() As [ILibraryInfo()](topic2055.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ILibraryManager](topic2079.md)
    Dim value() As [ILibraryInfo](topic2055.md)
     
    value = instance.GetLibraries()  
  
C#|   
---|---  
      
    
    [ILibraryInfo[]](topic2055.md) GetLibraries()  
  
#### Return Value

An array of information about the loaded libraries.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ILibraryManager Interface](topic2079.md)   
[ILibraryManager Members](topic2080.md)


