Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
HandleException(Exception) Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IExceptionHandler Interface](topic207.md) > [HandleException Method](topic212.md) : HandleException(Exception) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_ex_
    The exception.

Glossary Item Box

Handles the specified exception and returns true if it was handled. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Overloads Function HandleException( _
       ByVal _ex_ As Exception _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IExceptionHandler](topic207.md)
    Dim ex As Exception
    Dim value As Boolean
     
    value = instance.HandleException(ex)  
  
C#|   
---|---  
      
    
    bool HandleException( 
       Exception _ex_
    )  
  
#### Parameters

 _ex_
    The exception.

#### Return Value

True if the exception was handled and can be safely ignored, false to rethrow it.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IExceptionHandler Interface](topic207.md)   
[IExceptionHandler Members](topic208.md)   
[Overload List](topic212.md)


