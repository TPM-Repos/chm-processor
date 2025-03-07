Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GeneratePreviewCore Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [WordDocument Class](topic5885.md) : GeneratePreviewCore Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_previewDirectory_
    

_results_
    

Glossary Item Box

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overrides Function GeneratePreviewCore( _
       ByVal _previewDirectory_ As String, _
       ByVal _results_ As [RuleResults](topic11136.md) _
    ) As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [WordDocument](topic5885.md)
    Dim previewDirectory As String
    Dim results As [RuleResults](topic11136.md)
    Dim value As String
     
    value = instance.GeneratePreviewCore(previewDirectory, results)  
  
C#|   
---|---  
      
    
    protected override string GeneratePreviewCore( 
       string _previewDirectory_ ,
       [RuleResults](topic11136.md) _results_
    )  
  
#### Parameters

 _previewDirectory_
    
_results_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[WordDocument Class](topic5885.md)   
[WordDocument Members](topic5886.md)


