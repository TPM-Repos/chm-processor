Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ProhibitedStatesAttribute Class   
[Members](topic13876.md)   
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) : ProhibitedStatesAttribute Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

An attribute used to flag all prohibited the application states where this entity should not be visible if the application is in any of them. 

# Object Model

![](dotnetdiagramimages/image763.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <EditorBrowsableAttribute(EditorBrowsableState.Advanced)>
    <AttributeUsageAttribute(ValidOn=AttributeTargets.Class, 
       AllowMultiple=False, 
       Inherited=True)>
    Public Class ProhibitedStatesAttribute 
       Inherits System.Attribute  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProhibitedStatesAttribute](topic13875.md)  
  
C#|   
---|---  
      
    
    [EditorBrowsableAttribute(EditorBrowsableState.Advanced)]
    [AttributeUsageAttribute(ValidOn=AttributeTargets.Class, 
       AllowMultiple=false, 
       Inherited=true)]
    public class ProhibitedStatesAttribute : System.Attribute   
  
# Inheritance Hierarchy

System.Object  
System.Attribute  
**DriveWorks.SolidWorks.ProhibitedStatesAttribute**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProhibitedStatesAttribute Members](topic13876.md)   
[DriveWorks.SolidWorks Namespace](topic13345.md)


