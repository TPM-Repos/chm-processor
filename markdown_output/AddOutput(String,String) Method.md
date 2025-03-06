![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddOutput(String,String) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4076.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectChildSpecificationProjectDef Class](topic4067.md) > [AddOutput Method](topic4075.md) : AddOutput(String,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_localColumnName_
    The local column name to bind.

_remoteVariableName_
    The Name of the variable to bind the column to.

Glossary Item Box

Adds a new output binging to this project definition. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function AddOutput( _
       ByVal _localColumnName_ As String, _
       ByVal _remoteVariableName_ As String _
    ) As [ProjectChildSpecificationOutputDef](topic4056.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectChildSpecificationProjectDef](topic4067.md)
    Dim localColumnName As String
    Dim remoteVariableName As String
    Dim value As [ProjectChildSpecificationOutputDef](topic4056.md)
     
    value = instance.AddOutput(localColumnName, remoteVariableName)  
  
C#|   
---|---  
      
    
    public [ProjectChildSpecificationOutputDef](topic4056.md) AddOutput( 
       string _localColumnName_ ,
       string _remoteVariableName_
    )  
  
#### Parameters

 _localColumnName_
    The local column name to bind.
_remoteVariableName_
    The Name of the variable to bind the column to.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectChildSpecificationProjectDef Class](topic4067.md)   
[ProjectChildSpecificationProjectDef Members](topic4068.md)   
[Overload List](topic4075.md)

©2024 DriveWorks Ltd. All Rights Reserved.
