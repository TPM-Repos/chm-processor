       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RemoveProjectDefinition Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4038.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectChildSpecificationDef Class](topic4019.md) : RemoveProjectDefinition Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_ChildSpecProjectDefinition_
    The project definition to remove from the child specification list.

Glossary Item Box

Removes a project definition from the item list. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub RemoveProjectDefinition( _
       ByVal _ChildSpecProjectDefinition_ As [ProjectChildSpecificationProjectDef](topic4067.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectChildSpecificationDef](topic4019.md)
    Dim ChildSpecProjectDefinition As [ProjectChildSpecificationProjectDef](topic4067.md)
     
    instance.RemoveProjectDefinition(ChildSpecProjectDefinition)  
  
C#|   
---|---  
      
    
    public void RemoveProjectDefinition( 
       [ProjectChildSpecificationProjectDef](topic4067.md) _ChildSpecProjectDefinition_
    )  
  
#### Parameters

 _ChildSpecProjectDefinition_
    The project definition to remove from the child specification list.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectChildSpecificationDef Class](topic4019.md)   
[ProjectChildSpecificationDef Members](topic4020.md)

©2024 DriveWorks Ltd. All Rights Reserved.
