![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddOutput(String,String,ProjectChildSpecificationOutputType) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectChildSpecificationProjectDef Class](topic4067.md) > [AddOutput Method](topic4075.md) : AddOutput(String,String,ProjectChildSpecificationOutputType) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_localColumnName_
    The local column name to bind.

_outputDisplayName_
    The display name of the output to which the column will be bound.

_outputType_
    The type of output.

Glossary Item Box

Adds a new output binding to this project definition. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function AddOutput( _
       ByVal _localColumnName_ As String, _
       ByVal _outputDisplayName_ As String, _
       ByVal _outputType_ As [ProjectChildSpecificationOutputType](topic2357.md) _
    ) As [ProjectChildSpecificationOutputDef](topic4056.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectChildSpecificationProjectDef](topic4067.md)
    Dim localColumnName As String
    Dim outputDisplayName As String
    Dim outputType As [ProjectChildSpecificationOutputType](topic2357.md)
    Dim value As [ProjectChildSpecificationOutputDef](topic4056.md)
     
    value = instance.AddOutput(localColumnName, outputDisplayName, outputType)  
  
C#|   
---|---  
      
    
    public [ProjectChildSpecificationOutputDef](topic4056.md) AddOutput( 
       string _localColumnName_ ,
       string _outputDisplayName_ ,
       [ProjectChildSpecificationOutputType](topic2357.md) _outputType_
    )  
  
#### Parameters

 _localColumnName_
    The local column name to bind.
_outputDisplayName_
    The display name of the output to which the column will be bound.
_outputType_
    The type of output.

#### Return Value

The child specification output.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectChildSpecificationProjectDef Class](topic4067.md)   
[ProjectChildSpecificationProjectDef Members](topic4068.md)   
[Overload List](topic4075.md)


