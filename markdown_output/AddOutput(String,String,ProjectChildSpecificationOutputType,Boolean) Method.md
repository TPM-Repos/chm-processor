Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddOutput(String,String,ProjectChildSpecificationOutputType,Boolean) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectChildSpecificationProjectDef Class](topic4067.md) > [AddOutput Method](topic4075.md) : AddOutput(String,String,ProjectChildSpecificationOutputType,Boolean) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_localColumnName_
    The local column name to bind.

_outputDisplayName_
    The display name of the output to which the column will be bound. This could be an empty string if it is to be auto mapped based on the column name.

_outputType_
    The type of output.

_autoMap_
    Whether this column should be mapped automatically to a specification property with the same name.

Glossary Item Box

Adds a new output binding to this project definition. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function AddOutput( _
       ByVal _localColumnName_ As String, _
       ByVal _outputDisplayName_ As String, _
       ByVal _outputType_ As [ProjectChildSpecificationOutputType](topic2357.md), _
       ByVal _autoMap_ As Boolean _
    ) As [ProjectChildSpecificationOutputDef](topic4056.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectChildSpecificationProjectDef](topic4067.md)
    Dim localColumnName As String
    Dim outputDisplayName As String
    Dim outputType As [ProjectChildSpecificationOutputType](topic2357.md)
    Dim autoMap As Boolean
    Dim value As [ProjectChildSpecificationOutputDef](topic4056.md)
     
    value = instance.AddOutput(localColumnName, outputDisplayName, outputType, autoMap)  
  
C#|   
---|---  
      
    
    public [ProjectChildSpecificationOutputDef](topic4056.md) AddOutput( 
       string _localColumnName_ ,
       string _outputDisplayName_ ,
       [ProjectChildSpecificationOutputType](topic2357.md) _outputType_ ,
       bool _autoMap_
    )  
  
#### Parameters

 _localColumnName_
    The local column name to bind.
_outputDisplayName_
    The display name of the output to which the column will be bound. This could be an empty string if it is to be auto mapped based on the column name.
_outputType_
    The type of output.
_autoMap_
    Whether this column should be mapped automatically to a specification property with the same name.

#### Return Value

The child specification output.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectChildSpecificationProjectDef Class](topic4067.md)   
[ProjectChildSpecificationProjectDef Members](topic4068.md)   
[Overload List](topic4075.md)


