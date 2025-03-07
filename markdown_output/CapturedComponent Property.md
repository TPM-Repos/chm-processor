Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CapturedComponent Property   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [ISolidWorksState Interface](topic13419.md) : CapturedComponent Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets the capture information for the current model. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Property CapturedComponent As [CapturedSolidWorksComponent](topic14343.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ISolidWorksState](topic13419.md)
    Dim value As [CapturedSolidWorksComponent](topic14343.md)
     
    instance.CapturedComponent = value
     
    value = instance.CapturedComponent  
  
C#|   
---|---  
      
    
    [CapturedSolidWorksComponent](topic14343.md) CapturedComponent {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ISolidWorksState Interface](topic13419.md)   
[ISolidWorksState Members](topic13420.md)


