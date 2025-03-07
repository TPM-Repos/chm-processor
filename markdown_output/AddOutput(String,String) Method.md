Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddOutput(String,String) Method   
  
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

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function AddOutput( _
       ByVal _localColumnName_ As String, _
       ByVal _remoteVariableName_ As String _
    ) As [ProjectChildSpecificationOutputDef](topic4056.md)  
  
Visual Basic (Usage)| Copy Code  
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

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectChildSpecificationProjectDef Class](topic4067.md)   
[ProjectChildSpecificationProjectDef Members](topic4068.md)   
[Overload List](topic4075.md)


