Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FeatureDriveCompatibilityVersion Property   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation Namespace](topic15094.md) > [GenerationSettings Class](topic15238.md) : FeatureDriveCompatibilityVersion Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets the compatibility version used to drive feature parameters, 0 means to drive features in the exact way as DriveWorks 7 and 8, 1 means to drive features using DriveWorks 9's semantics - i.e. Hole Wizard features are driven using user units rather than system units. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property FeatureDriveCompatibilityVersion As Integer  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GenerationSettings](topic15238.md)
    Dim value As Integer
     
    instance.FeatureDriveCompatibilityVersion = value
     
    value = instance.FeatureDriveCompatibilityVersion  
  
C#|   
---|---  
      
    
    public int FeatureDriveCompatibilityVersion {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GenerationSettings Class](topic15238.md)   
[GenerationSettings Members](topic15239.md)


