Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
EffectivePreviewResult Constructor(String,IEnumerable<String>)   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [EffectivePreviewResult Class](topic8075.md) > [EffectivePreviewResult Constructor](topic8081.md) : EffectivePreviewResult Constructor(String,IEnumerable<String>)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_previewFilePath_
    The fully qualified path to the preview file.

_supportingFilePaths_
    A collection of fully qualified paths to additional files that belong to the preview and may be requested.

Glossary Item Box

Initializes a new instance of an effective preview result. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _previewFilePath_ As String, _
       ByVal _supportingFilePaths_ As IEnumerable(Of String) _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim previewFilePath As String
    Dim supportingFilePaths As IEnumerable(Of String)
     
    Dim instance As New [EffectivePreviewResult](topic8075.md)(previewFilePath, supportingFilePaths)  
  
C#|   
---|---  
      
    
    public EffectivePreviewResult( 
       string _previewFilePath_ ,
       IEnumerable<string> _supportingFilePaths_
    )  
  
#### Parameters

 _previewFilePath_
    The fully qualified path to the preview file.
_supportingFilePaths_
    A collection of fully qualified paths to additional files that belong to the preview and may be requested.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[EffectivePreviewResult Class](topic8075.md)   
[EffectivePreviewResult Members](topic8076.md)   
[Overload List](topic8081.md)


