Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ItemsChanged Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectItemListDef Class](topic4511.md) : ItemsChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when any items have been added/deleted/edited/moved. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event ItemsChanged As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectItemListDef](topic4511.md)
    Dim handler As EventHandler
     
    AddHandler instance.ItemsChanged, handler  
  
C#|   
---|---  
      
    
    public event EventHandler ItemsChanged  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectItemListDef Class](topic4511.md)   
[ProjectItemListDef Members](topic4512.md)


