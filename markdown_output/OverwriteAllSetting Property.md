Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
OverwriteAllSetting Property   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation.Unified Namespace](topic15343.md) > [DiagnosticPreparationInteraction Class](topic15345.md) : OverwriteAllSetting Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

The saved 'Overwrite All' models user setting. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property OverwriteAllSetting As Nullable(Of Boolean)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DiagnosticPreparationInteraction](topic15345.md)
    Dim value As Nullable(Of Boolean)
     
    instance.OverwriteAllSetting = value
     
    value = instance.OverwriteAllSetting  
  
C#|   
---|---  
      
    
    public Nullable<bool> OverwriteAllSetting {get; set;}  
  
#### Property Value

Nothing if no setting was saved, True to overwrite all models, False to re-generate all models.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DiagnosticPreparationInteraction Class](topic15345.md)   
[DiagnosticPreparationInteraction Members](topic15346.md)


