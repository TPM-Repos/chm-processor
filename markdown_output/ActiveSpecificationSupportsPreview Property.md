Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ActiveSpecificationSupportsPreview Property   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [ISpecificationsManager Interface](topic13440.md) : ActiveSpecificationSupportsPreview Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Determines if the current specification supports OnDemand previews, if no specification is active or the specification doesn't support preview, false is returned. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    ReadOnly Property ActiveSpecificationSupportsPreview As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ISpecificationsManager](topic13440.md)
    Dim value As Boolean
     
    value = instance.ActiveSpecificationSupportsPreview  
  
C#|   
---|---  
      
    
    bool ActiveSpecificationSupportsPreview {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ISpecificationsManager Interface](topic13440.md)   
[ISpecificationsManager Members](topic13441.md)


