       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
WizardRunningException Constructor(String,Exception)   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [WizardRunningException Class](topic1257.md) > [WizardRunningException Constructor](topic1263.md) : WizardRunningException Constructor(String,Exception)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_message_
    The exception message.

_inner_
    The inner exception.

Glossary Item Box

Creates an instance of the [WizardRunningException](topic1257.md) class. 

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
     
    Dim instance As New [WizardRunningException](topic1257.md)(message, inner)  
  
C#|   
---|---  
      
    
    public WizardRunningException( 
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

[WizardRunningException Class](topic1257.md)   
[WizardRunningException Members](topic1258.md)   
[Overload List](topic1263.md)


