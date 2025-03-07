Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GenerationFailedException Constructor(String,Exception)   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation Namespace](topic15094.md) > [GenerationFailedException Class](topic15228.md) > [GenerationFailedException Constructor](topic15234.md) : GenerationFailedException Constructor(String,Exception)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_message_
    A description of the exception.

_inner_
    The inner exception.

Glossary Item Box

Initializes an instance of the [GenerationFailedException](topic15228.md) class. 

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
     
    Dim instance As New [GenerationFailedException](topic15228.md)(message, inner)  
  
C#|   
---|---  
      
    
    public GenerationFailedException( 
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

[GenerationFailedException Class](topic15228.md)   
[GenerationFailedException Members](topic15229.md)   
[Overload List](topic15234.md)


