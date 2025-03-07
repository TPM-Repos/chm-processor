Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ComponentRegisteredWithDifferentPathException Constructor(String,Exception)   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [ComponentRegisteredWithDifferentPathException Class](topic13517.md) > [ComponentRegisteredWithDifferentPathException Constructor](topic13523.md) : ComponentRegisteredWithDifferentPathException Constructor(String,Exception)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_message_
    The exception message.

_inner_
    The inner exception.

Glossary Item Box

Initializes a new instance of the [ComponentRegisteredWithDifferentPathException](topic13517.md) exception class. 

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
     
    Dim instance As New [ComponentRegisteredWithDifferentPathException](topic13517.md)(message, inner)  
  
C#|   
---|---  
      
    
    public ComponentRegisteredWithDifferentPathException( 
       string _message_ ,
       Exception _inner_
    )  
  
#### Parameters

 _message_
    The exception message.
_inner_
    The inner exception.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ComponentRegisteredWithDifferentPathException Class](topic13517.md)   
[ComponentRegisteredWithDifferentPathException Members](topic13518.md)   
[Overload List](topic13523.md)


