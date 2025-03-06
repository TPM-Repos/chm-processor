![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddInput Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6763.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Connectors.Database Namespace](topic6754.md) > [DatabaseConnectorConfiguration Class](topic6756.md) : AddInput Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_fieldName_
    The database field name to bind to.

_inputName_
    The DriveWorks input name to bind to.

Glossary Item Box

Adds a new input bindings for this configuration. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub AddInput( _
       ByVal _fieldName_ As String, _
       ByVal _inputName_ As String _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [DatabaseConnectorConfiguration](topic6756.md)
    Dim fieldName As String
    Dim inputName As String
     
    instance.AddInput(fieldName, inputName)  
  
C#|   
---|---  
      
    
    public void AddInput( 
       string _fieldName_ ,
       string _inputName_
    )  
  
#### Parameters

 _fieldName_
    The database field name to bind to.
_inputName_
    The DriveWorks input name to bind to.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[DatabaseConnectorConfiguration Class](topic6756.md)   
[DatabaseConnectorConfiguration Members](topic6757.md)

©2024 DriveWorks Ltd. All Rights Reserved.
