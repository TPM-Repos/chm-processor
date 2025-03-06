![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryGetTypeFromLibrary Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2089.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Extensibility Namespace](topic1995.md) > [ILibraryManager Interface](topic2079.md) : TryGetTypeFromLibrary Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_fullTypeName_
    The type string which identifies the name of the type and its parent library.

_result_
    Receives the specified type.

Glossary Item Box

Gets a type from a library. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function TryGetTypeFromLibrary( _
       ByVal _fullTypeName_ As String, _
       ByRef _result_ As Type _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ILibraryManager](topic2079.md)
    Dim fullTypeName As String
    Dim result As Type
    Dim value As Boolean
     
    value = instance.TryGetTypeFromLibrary(fullTypeName, result)  
  
C#|   
---|---  
      
    
    bool TryGetTypeFromLibrary( 
       string _fullTypeName_ ,
       ref Type _result_
    )  
  
#### Parameters

 _fullTypeName_
    The type string which identifies the name of the type and its parent library.
_result_
    Receives the specified type.

#### Return Value

True if the specified type was found and returned, otherwise false.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ILibraryManager Interface](topic2079.md)   
[ILibraryManager Members](topic2080.md)

©2024 DriveWorks Ltd. All Rights Reserved.
