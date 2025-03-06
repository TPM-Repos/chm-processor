![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CommandInvocationException Constructor(String,Exception)   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [CommandInvocationException Class](topic681.md) > [CommandInvocationException Constructor](topic687.md) : CommandInvocationException Constructor(String,Exception)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_errorMessage_
    

_inner_
    

Glossary Item Box

Creates a new instance of the [CommandInvocationException](topic681.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _errorMessage_ As String, _
       ByVal _inner_ As Exception _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim errorMessage As String
    Dim inner As Exception
     
    Dim instance As New [CommandInvocationException](topic681.md)(errorMessage, inner)  
  
C#|   
---|---  
      
    
    public CommandInvocationException( 
       string _errorMessage_ ,
       Exception _inner_
    )  
  
#### Parameters

 _errorMessage_
    
_inner_
    

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[CommandInvocationException Class](topic681.md)   
[CommandInvocationException Members](topic682.md)   
[Overload List](topic687.md)


