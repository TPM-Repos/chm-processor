![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetLibrary Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Extensibility Namespace](topic1995.md) > [ILibraryManager Interface](topic2079.md) : GetLibrary Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_invariantName_
    The invariant name of the library to retrieve.

_throwOnError_
    True to throw an error if the type cannot be found, false to return a null reference (Nothing in Visual Basic).

Glossary Item Box

Gets the library with the specified invariant name. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetLibrary( _
       ByVal _invariantName_ As String, _
       ByVal _throwOnError_ As Boolean _
    ) As [ILibraryInfo](topic2055.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ILibraryManager](topic2079.md)
    Dim invariantName As String
    Dim throwOnError As Boolean
    Dim value As [ILibraryInfo](topic2055.md)
     
    value = instance.GetLibrary(invariantName, throwOnError)  
  
C#|   
---|---  
      
    
    [ILibraryInfo](topic2055.md) GetLibrary( 
       string _invariantName_ ,
       bool _throwOnError_
    )  
  
#### Parameters

 _invariantName_
    The invariant name of the library to retrieve.
_throwOnError_
    True to throw an error if the type cannot be found, false to return a null reference (Nothing in Visual Basic).

#### Return Value

The specified library.

# ![](dotnetimages/collapse.gif)Exceptions

Exception| Description  
---|---  
[DriveWorks.ItemNotFoundException](topic3571.md)| The specified library could not be found.  
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ILibraryManager Interface](topic2079.md)   
[ILibraryManager Members](topic2080.md)


