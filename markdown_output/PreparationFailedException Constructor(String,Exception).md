Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
PreparationFailedException Constructor(String,Exception)   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation Namespace](topic15094.md) > [PreparationFailedException Class](topic15281.md) > [PreparationFailedException Constructor](topic15287.md) : PreparationFailedException Constructor(String,Exception)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_message_
    A description of the exception.

_inner_
    The inner exception.

Glossary Item Box

Initializes an instance of the [PreparationFailedException](topic15281.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _message_ As String, _
       ByVal _inner_ As Exception _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim message As String
    Dim inner As Exception
     
    Dim instance As New [PreparationFailedException](topic15281.md)(message, inner)  
  
C#|   
---|---  
      
    
    public PreparationFailedException( 
       string _message_ ,
       Exception _inner_
    )  
  
#### Parameters

 _message_
    A description of the exception.
_inner_
    The inner exception.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[PreparationFailedException Class](topic15281.md)   
[PreparationFailedException Members](topic15282.md)   
[Overload List](topic15287.md)


