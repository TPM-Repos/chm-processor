TryGetOutput Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectChildSpecificationProjectDef Class](topic4067.md) : TryGetOutput Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_columnName_
    Name of the item column to get the output for.

_output_
    The output to be set.

Glossary Item Box

Attempts to get a specified output from the given column name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryGetOutput( _
       ByVal _columnName_ As String, _
       ByRef _output_ As [ProjectChildSpecificationOutputDef](topic4056.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectChildSpecificationProjectDef](topic4067.md)
    Dim columnName As String
    Dim output As [ProjectChildSpecificationOutputDef](topic4056.md)
    Dim value As Boolean
     
    value = instance.TryGetOutput(columnName, output)  
  
C#|   
---|---  
      
    
    public bool TryGetOutput( 
       string _columnName_ ,
       ref [ProjectChildSpecificationOutputDef](topic4056.md) _output_
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

[ProjectChildSpecificationProjectDef Class](topic4067.md)   
[ProjectChildSpecificationProjectDef Members](topic4068.md)


