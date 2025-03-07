Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ActiveSite Property   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IApplicationSelectionManager Interface](topic59.md) : ActiveSite Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the active selection site in the application. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    ReadOnly Property ActiveSite As [ISelectionSite](topic422.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IApplicationSelectionManager](topic59.md)
    Dim value As [ISelectionSite](topic422.md)
     
    value = instance.ActiveSite  
  
C#|   
---|---  
      
    
    [ISelectionSite](topic422.md) ActiveSite {get;}  
  
#### Property Value

The active selection site, or a null reference (Nothing in Visual Basic) if no selection site is available.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IApplicationSelectionManager Interface](topic59.md)   
[IApplicationSelectionManager Members](topic60.md)


