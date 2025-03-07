Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetTableReferenceName Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectCalculationTable Class](topic3926.md) : GetTableReferenceName Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_displayName_
    The name to convert.

Glossary Item Box

Converts a table display name to a reference name (how it would be used in rules). 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function GetTableReferenceName( _
       ByVal _displayName_ As String _
    ) As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim displayName As String
    Dim value As String
     
    value = [ProjectCalculationTable](topic3926.md).GetTableReferenceName(displayName)  
  
C#|   
---|---  
      
    
    public static string GetTableReferenceName( 
       string _displayName_
    )  
  
#### Parameters

 _displayName_
    The name to convert.

#### Return Value

The converted name.

# Remarks

E.g. "Hello There" would return "DWCalcHelloThere"

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectCalculationTable Class](topic3926.md)   
[ProjectCalculationTable Members](topic3927.md)


