![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DelaySolidWorksResponsivenessCheck Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [ISolidWorksHealthMonitor Interface](topic1741.md) : DelaySolidWorksResponsivenessCheck Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_delay_
    The amount of time to wait until checking for SolidWorks responsiveness.

Glossary Item Box

Delays the SolidWorks responsiveness check for the specified amount of time. The time span will be added to the current system time to determine when the check should next be performed. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub DelaySolidWorksResponsivenessCheck( _
       ByVal _delay_ As TimeSpan _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ISolidWorksHealthMonitor](topic1741.md)
    Dim delay As TimeSpan
     
    instance.DelaySolidWorksResponsivenessCheck(delay)  
  
C#|   
---|---  
      
    
    void DelaySolidWorksResponsivenessCheck( 
       TimeSpan _delay_
    )  
  
#### Parameters

 _delay_
    The amount of time to wait until checking for SolidWorks responsiveness.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ISolidWorksHealthMonitor Interface](topic1741.md)   
[ISolidWorksHealthMonitor Members](topic1742.md)


