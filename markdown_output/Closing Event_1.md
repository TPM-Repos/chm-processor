Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Closing Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IApplication Interface](topic24.md) : Closing Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the application is being closed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event Closing As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IApplication](topic24.md)
    Dim handler As EventHandler
     
    AddHandler instance.Closing, handler  
  
C#|   
---|---  
      
    
    event EventHandler Closing  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IApplication Interface](topic24.md)   
[IApplication Members](topic25.md)


