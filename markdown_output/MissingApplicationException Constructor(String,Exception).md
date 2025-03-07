Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
MissingApplicationException Constructor(String,Exception)   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [MissingApplicationException Class](topic3715.md) > [MissingApplicationException Constructor](topic3721.md) : MissingApplicationException Constructor(String,Exception)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_applicationName_
    The name the of application is that is missing.

_innerException_
    The source exception.

Glossary Item Box

Creates a new instance of the [MissingApplicationException](topic3715.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _applicationName_ As String, _
       ByVal _innerException_ As Exception _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim applicationName As String
    Dim innerException As Exception
     
    Dim instance As New [MissingApplicationException](topic3715.md)(applicationName, innerException)  
  
C#|   
---|---  
      
    
    public MissingApplicationException( 
       string _applicationName_ ,
       Exception _innerException_
    )  
  
#### Parameters

 _applicationName_
    The name the of application is that is missing.
_innerException_
    The source exception.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[MissingApplicationException Class](topic3715.md)   
[MissingApplicationException Members](topic3716.md)   
[Overload List](topic3721.md)


