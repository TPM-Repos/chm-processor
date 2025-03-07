Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GeneratePreview(String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectDocument Class](topic4356.md) > [GeneratePreview Method](topic4374.md) : GeneratePreview(String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_previewDirectory_
    A fully-qualified path to a directory in which the preview file should be created.

Glossary Item Box

Creates a preview of the document in the specified directory. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function GeneratePreview( _
       ByVal _previewDirectory_ As String _
    ) As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectDocument](topic4356.md)
    Dim previewDirectory As String
    Dim value As String
     
    value = instance.GeneratePreview(previewDirectory)  
  
C#|   
---|---  
      
    
    public string GeneratePreview( 
       string _previewDirectory_
    )  
  
#### Parameters

 _previewDirectory_
    A fully-qualified path to a directory in which the preview file should be created.

#### Return Value

The full path to the preview file.

# Exceptions

Exception| Description  
---|---  
System.NotSupportedException| Thrown if the document does not support previewing, as indicated by the [SupportsPreview](topic4396.md) property.  
System.NotImplementedException| Thrown if the document has specified support for previewing, but has not overridden the [GeneratePreviewCore](topic4377.md) method.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectDocument Class](topic4356.md)   
[ProjectDocument Members](topic4357.md)   
[Overload List](topic4374.md)


