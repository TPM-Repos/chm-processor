Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetUrl(String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Abstractions Namespace](topic5939.md) > [IResourceUrlProvider Interface](topic5993.md) > [GetUrl Method](topic5998.md) : GetUrl(String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_resourcePath_
    The full path to the file.

Glossary Item Box

Gets the URL for the specified file. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Overloads Function GetUrl( _
       ByVal _resourcePath_ As String _
    ) As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IResourceUrlProvider](topic5993.md)
    Dim resourcePath As String
    Dim value As String
     
    value = instance.GetUrl(resourcePath)  
  
C#|   
---|---  
      
    
    string GetUrl( 
       string _resourcePath_
    )  
  
#### Parameters

 _resourcePath_
    The full path to the file.

#### Return Value

The URL to the specified file.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IResourceUrlProvider Interface](topic5993.md)   
[IResourceUrlProvider Members](topic5994.md)   
[Overload List](topic5998.md)


