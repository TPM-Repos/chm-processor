Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GroupOpened Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IGroupService Interface](topic251.md) : GroupOpened Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a group is opened. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event GroupOpened As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IGroupService](topic251.md)
    Dim handler As EventHandler
     
    AddHandler instance.GroupOpened, handler  
  
C#|   
---|---  
      
    
    event EventHandler GroupOpened  
  
# Remarks

This event will not be fired if the group could not be opened.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IGroupService Interface](topic251.md)   
[IGroupService Members](topic252.md)


