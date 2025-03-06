       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetNamedItemValues Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3884.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Project Class](topic3859.md) : SetNamedItemValues Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_namesAndValues_
    The named items and values to set.

Glossary Item Box

Sets the values of the specified named items. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <EditorBrowsableAttribute(EditorBrowsableState.Advanced)>
    Public Function SetNamedItemValues( _
       ByVal _namesAndValues_ As IEnumerable(Of KeyValuePair(Of String,String)) _
    ) As String()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Project](topic3859.md)
    Dim namesAndValues As IEnumerable(Of KeyValuePair(Of String,String))
    Dim value() As String
     
    value = instance.SetNamedItemValues(namesAndValues)  
  
C#|   
---|---  
      
    
    [EditorBrowsableAttribute(EditorBrowsableState.Advanced)]
    public string[] SetNamedItemValues( 
       IEnumerable<KeyValuePair<string,string>> _namesAndValues_
    )  
  
#### Parameters

 _namesAndValues_
    The named items and values to set.

#### Return Value

The names of any items that could not be driven.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Project Class](topic3859.md)   
[Project Members](topic3860.md)

©2024 DriveWorks Ltd. All Rights Reserved.
