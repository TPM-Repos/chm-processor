Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FeatureDeleteDisabled Property   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation Namespace](topic15094.md) > [GenerationSettings Class](topic15238.md) : FeatureDeleteDisabled Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets or sets whether feature deletion is disabled. If feature deletion is disabled then features which should be deleted will be suppressed instead. This property is not locked. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property FeatureDeleteDisabled As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GenerationSettings](topic15238.md)
    Dim value As Boolean
     
    instance.FeatureDeleteDisabled = value
     
    value = instance.FeatureDeleteDisabled  
  
C#|   
---|---  
      
    
    public bool FeatureDeleteDisabled {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GenerationSettings Class](topic15238.md)   
[GenerationSettings Members](topic15239.md)


