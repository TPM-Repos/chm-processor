Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GroupClosed Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IGroupService Interface](topic251.md) : GroupClosed Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the active group is closed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event GroupClosed As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IGroupService](topic251.md)
    Dim handler As EventHandler
     
    AddHandler instance.GroupClosed, handler  
  
C#|   
---|---  
      
    
    event EventHandler GroupClosed  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IGroupService Interface](topic251.md)   
[IGroupService Members](topic252.md)


