       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ShouldOverwriteExistingNonGeneratedTarget Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation.Unified Namespace](topic15343.md) > [DiagnosticPreparationInteraction Class](topic15345.md) : ShouldOverwriteExistingNonGeneratedTarget Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_targetPath_
    The file-path of the existing non-generated file.

Glossary Item Box

Retrieves a saved 'Overwrite All' setting and/or prompts the user via a dialog as whether to overwrite the existing non-generated target. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function ShouldOverwriteExistingNonGeneratedTarget( _
       ByVal _targetPath_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DiagnosticPreparationInteraction](topic15345.md)
    Dim targetPath As String
    Dim value As Boolean
     
    value = instance.ShouldOverwriteExistingNonGeneratedTarget(targetPath)  
  
C#|   
---|---  
      
    
    public bool ShouldOverwriteExistingNonGeneratedTarget( 
       string _targetPath_
    )  
  
#### Parameters

 _targetPath_
    The file-path of the existing non-generated file.

#### Return Value

True if the file should be overwritten, otherwise False.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DiagnosticPreparationInteraction Class](topic15345.md)   
[DiagnosticPreparationInteraction Members](topic15346.md)


