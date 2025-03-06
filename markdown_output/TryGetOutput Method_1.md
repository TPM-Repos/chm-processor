       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryGetOutput Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectItemListTypeDef Class](topic4533.md) : TryGetOutput Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_columnName_
    Name of the item column to get the output for.

_output_
    The output to be set.

Glossary Item Box

Attempts to get a specified output from the given item type column name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryGetOutput( _
       ByVal _columnName_ As String, _
       ByRef _output_ As [ProjectItemListTypeOutputDef](topic4547.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectItemListTypeDef](topic4533.md)
    Dim columnName As String
    Dim output As [ProjectItemListTypeOutputDef](topic4547.md)
    Dim value As Boolean
     
    value = instance.TryGetOutput(columnName, output)  
  
C#|   
---|---  
      
    
    public bool TryGetOutput( 
       string _columnName_ ,
       ref [ProjectItemListTypeOutputDef](topic4547.md) _output_
    )  
  
#### Parameters

 _columnName_
    Name of the item column to get the output for.
_output_
    The output to be set.

#### Return Value

True if the output was found.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectItemListTypeDef Class](topic4533.md)   
[ProjectItemListTypeDef Members](topic4534.md)


