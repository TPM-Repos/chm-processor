![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AgentDetails Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2387.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [AgentDetails Class](topic2381.md) : AgentDetails Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_machineName_
    The name of the machine for this agent.

_operatingSystem_
    The operating system for this agent.

_processorArchitecture_
    The processor architecture for this agent.

Glossary Item Box

Creates a new instance of the AgentDetails class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _machineName_ As String, _
       ByVal _operatingSystem_ As String, _
       ByVal _processorArchitecture_ As String _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim machineName As String
    Dim operatingSystem As String
    Dim processorArchitecture As String
     
    Dim instance As New [AgentDetails](topic2381.md)(machineName, operatingSystem, processorArchitecture)  
  
C#|   
---|---  
      
    
    public AgentDetails( 
       string _machineName_ ,
       string _operatingSystem_ ,
       string _processorArchitecture_
    )  
  
#### Parameters

 _machineName_
    The name of the machine for this agent.
_operatingSystem_
    The operating system for this agent.
_processorArchitecture_
    The processor architecture for this agent.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[AgentDetails Class](topic2381.md)   
[AgentDetails Members](topic2382.md)

©2024 DriveWorks Ltd. All Rights Reserved.
