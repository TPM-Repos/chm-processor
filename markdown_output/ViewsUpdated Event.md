       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ViewsUpdated Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Extensibility Namespace](topic1995.md) > [IApplicationModule Interface](topic1997.md) : ViewsUpdated Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when views are updated. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event ViewsUpdated As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IApplicationModule](topic1997.md)
    Dim handler As EventHandler
     
    AddHandler instance.ViewsUpdated, handler  
  
C#|   
---|---  
      
    
    event EventHandler ViewsUpdated  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IApplicationModule Interface](topic1997.md)   
[IApplicationModule Members](topic1998.md)


