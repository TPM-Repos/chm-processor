Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ProcessAborted Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Refactoring Namespace](topic10266.md) > [RenameProcess Class](topic10287.md) : ProcessAborted Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the entire rename process is aborted. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event ProcessAborted As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [RenameProcess](topic10287.md)
    Dim handler As EventHandler
     
    AddHandler instance.ProcessAborted, handler  
  
C#|   
---|---  
      
    
    public event EventHandler ProcessAborted  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RenameProcess Class](topic10287.md)   
[RenameProcess Members](topic10288.md)


