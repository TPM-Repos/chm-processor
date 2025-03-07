Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CheckedFileExists Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [IAutopilotService Interface](topic1654.md) : CheckedFileExists Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when an Autopilot component such as a queue or connector has finished checking the existence of a file. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event CheckedFileExists As EventHandler(Of FileExistenceCheckEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IAutopilotService](topic1654.md)
    Dim handler As EventHandler(Of FileExistenceCheckEventArgs)
     
    AddHandler instance.CheckedFileExists, handler  
  
C#|   
---|---  
      
    
    event EventHandler<FileExistenceCheckEventArgs> CheckedFileExists  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IAutopilotService Interface](topic1654.md)   
[IAutopilotService Members](topic1655.md)


