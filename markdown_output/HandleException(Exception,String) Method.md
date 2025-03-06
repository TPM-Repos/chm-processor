![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
HandleException(Exception,String) Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IExceptionHandler Interface](topic207.md) > [HandleException Method](topic212.md) : HandleException(Exception,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_ex_
    The exception.

_source_
    The source of the exception.

Glossary Item Box

Handles the specified exception and returns true if it was handled. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Overloads Function HandleException( _
       ByVal _ex_ As Exception, _
       ByVal _source_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IExceptionHandler](topic207.md)
    Dim ex As Exception
    Dim source As String
    Dim value As Boolean
     
    value = instance.HandleException(ex, source)  
  
C#|   
---|---  
      
    
    bool HandleException( 
       Exception _ex_ ,
       string _source_
    )  
  
#### Parameters

 _ex_
    The exception.
_source_
    The source of the exception.

#### Return Value

True if the exception was handled and can be safely ignored, false to rethrow it.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IExceptionHandler Interface](topic207.md)   
[IExceptionHandler Members](topic208.md)   
[Overload List](topic212.md)


