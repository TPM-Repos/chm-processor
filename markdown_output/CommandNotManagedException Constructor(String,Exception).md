![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CommandNotManagedException Constructor(String,Exception)   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic707.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [CommandNotManagedException Class](topic699.md) > [CommandNotManagedException Constructor](topic705.md) : CommandNotManagedException Constructor(String,Exception)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_commandName_
    

_inner_
    

Glossary Item Box

Creates a new instance of the [CommandNotManagedException](topic699.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _commandName_ As String, _
       ByVal _inner_ As Exception _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim commandName As String
    Dim inner As Exception
     
    Dim instance As New [CommandNotManagedException](topic699.md)(commandName, inner)  
  
C#|   
---|---  
      
    
    public CommandNotManagedException( 
       string _commandName_ ,
       Exception _inner_
    )  
  
#### Parameters

 _commandName_
    
_inner_
    

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[CommandNotManagedException Class](topic699.md)   
[CommandNotManagedException Members](topic700.md)   
[Overload List](topic705.md)

©2024 DriveWorks Ltd. All Rights Reserved.
