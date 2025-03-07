Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GroupClosing Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IGroupService Interface](topic251.md) : GroupClosing Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the active group is about to be closed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event GroupClosing As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IGroupService](topic251.md)
    Dim handler As EventHandler
     
    AddHandler instance.GroupClosing, handler  
  
C#|   
---|---  
      
    
    event EventHandler GroupClosing  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IGroupService Interface](topic251.md)   
[IGroupService Members](topic252.md)


