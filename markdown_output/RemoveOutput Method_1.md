       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RemoveOutput Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4540.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectItemListTypeDef Class](topic4533.md) : RemoveOutput Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_output_
    The output binding to remove.

Glossary Item Box

Removes an output from this list of outputs. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub RemoveOutput( _
       ByVal _output_ As [ProjectItemListTypeOutputDef](topic4547.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectItemListTypeDef](topic4533.md)
    Dim output As [ProjectItemListTypeOutputDef](topic4547.md)
     
    instance.RemoveOutput(output)  
  
C#|   
---|---  
      
    
    public void RemoveOutput( 
       [ProjectItemListTypeOutputDef](topic4547.md) _output_
    )  
  
#### Parameters

 _output_
    The output binding to remove.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectItemListTypeDef Class](topic4533.md)   
[ProjectItemListTypeDef Members](topic4534.md)

©2024 DriveWorks Ltd. All Rights Reserved.
