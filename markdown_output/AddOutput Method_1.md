Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddOutput Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectItemListTypeDef Class](topic4533.md) : AddOutput Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_localColumnName_
    The local column name to bind.

_remoteControlName_
    The Name of the control to bind the column to.

Glossary Item Box

Adds a new output binging to this type definition. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function AddOutput( _
       ByVal _localColumnName_ As String, _
       ByVal _remoteControlName_ As String _
    ) As [ProjectItemListTypeOutputDef](topic4547.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectItemListTypeDef](topic4533.md)
    Dim localColumnName As String
    Dim remoteControlName As String
    Dim value As [ProjectItemListTypeOutputDef](topic4547.md)
     
    value = instance.AddOutput(localColumnName, remoteControlName)  
  
C#|   
---|---  
      
    
    public [ProjectItemListTypeOutputDef](topic4547.md) AddOutput( 
       string _localColumnName_ ,
       string _remoteControlName_
    )  
  
#### Parameters

 _localColumnName_
    The local column name to bind.
_remoteControlName_
    The Name of the control to bind the column to.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectItemListTypeDef Class](topic4533.md)   
[ProjectItemListTypeDef Members](topic4534.md)


